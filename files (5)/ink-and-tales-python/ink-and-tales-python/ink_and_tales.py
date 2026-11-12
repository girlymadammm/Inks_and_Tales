"""
Ink and Tales: desktop launcher.  Made by Ashki Studio.  Ideas into experiences.

What this does:
  1. Starts a tiny private web server that only your own computer can reach (127.0.0.1).
  2. Opens the app in its own window (Microsoft Edge, Chrome or Brave in "app mode": no tabs, no address bar).
  3. When you close the window, the server stops.

Your writing is saved in the folder shown by data_dir() below, so it stays on your device.
Run it directly with:   python ink_and_tales.py
Build the .exe with:     build_exe.bat   (Windows)
"""
import ctypes
import http.server
import os
import platform
import shutil
import socketserver
import subprocess
import sys
import threading
import time
import urllib.request
import webbrowser

APP_NAME = "Ink and Tales"
HOST = "127.0.0.1"
PORTS = range(47819, 47830)           # the app always tries the same port first so your saved writing is found again
HEALTH = "/__ink_and_tales__"


def base_dir():
    return getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))


APP_DIR = os.path.join(base_dir(), "app")


def data_dir():
    system = platform.system()
    if system == "Windows":
        root = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    elif system == "Darwin":
        root = os.path.expanduser("~/Library/Application Support")
    else:
        root = os.environ.get("XDG_DATA_HOME") or os.path.expanduser("~/.local/share")
    path = os.path.join(root, "InkAndTales")
    os.makedirs(path, exist_ok=True)
    return path


def log(message):
    try:
        with open(os.path.join(data_dir(), "launcher.log"), "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + str(message) + "\n")
    except Exception:
        pass


def say(title, message):
    """Show a message even when there is no console (the built .exe has none)."""
    if platform.system() == "Windows":
        try:
            ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)
            return
        except Exception:
            pass
    if sys.stdout:
        print(f"{title}: {message}")


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".webmanifest": "application/manifest+json"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=APP_DIR, **kwargs)

    def do_GET(self):
        if self.path.split("?")[0] == HEALTH:
            body = b"ok"
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, *args):
        pass


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    # Windows: never share a port between two programs. Mac/Linux: reuse is safe and lets you reopen the app right
    # after closing it (otherwise the port stays busy for a minute and your saved writing would seem to disappear).
    allow_reuse_address = platform.system() != "Windows"
    daemon_threads = True


def is_ours(port):
    try:
        with urllib.request.urlopen(f"http://{HOST}:{port}{HEALTH}", timeout=0.6) as r:
            return r.read() == b"ok"
    except Exception:
        return False


def start_server():
    """Returns (server or None, port, already_running)."""
    for port in PORTS:
        if is_ours(port):
            return None, port, True
        try:
            server = Server((HOST, port), Handler)
        except OSError:
            continue
        threading.Thread(target=server.serve_forever, daemon=True).start()
        return server, port, False
    raise RuntimeError("No free port found between %d and %d." % (PORTS[0], PORTS[-1]))


def find_browser():
    override = os.environ.get("INK_BROWSER")
    if override and os.path.exists(override):
        return override
    system = platform.system()
    if system == "Windows":
        roots = [os.environ.get(k) for k in ("PROGRAMFILES(X86)", "PROGRAMFILES", "LOCALAPPDATA")]
        rels = [r"Microsoft\Edge\Application\msedge.exe",
                r"Google\Chrome\Application\chrome.exe",
                r"BraveSoftware\Brave-Browser\Application\brave.exe"]
        for rel in rels:
            for root in roots:
                if root and os.path.exists(os.path.join(root, rel)):
                    return os.path.join(root, rel)
    elif system == "Darwin":
        for p in ("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
                  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                  "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"):
            if os.path.exists(p):
                return p
    else:
        for name in ("microsoft-edge", "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "brave-browser"):
            found = shutil.which(name)
            if found:
                return found
    return None


def open_window(browser, url):
    profile = os.path.join(data_dir(), "profile")          # your stories live here
    args = [browser, f"--app={url}", f"--user-data-dir={profile}",
            "--no-first-run", "--no-default-browser-check", "--window-size=1280,820"]
    args += os.environ.get("INK_EXTRA_ARGS", "").split()
    return subprocess.Popen(args)


def main():
    if not os.path.isdir(APP_DIR):
        say(APP_NAME, "The app files are missing (the 'app' folder was not found).")
        return 1
    server, port, already = start_server()
    url = f"http://{HOST}:{port}/"
    log(f"start port={port} already_running={already}")
    if port != PORTS[0] and not already:
        log("WARNING: the usual port was busy, so saved stories from the usual address will not show up in this window.")
        say(APP_NAME, "Another program is using Ink and Tales' usual address, so this window cannot see your saved stories.\n\n"
                      "Close the other program, then open Ink and Tales again.")

    if "--serve" in sys.argv:                                  # for testing: just serve, no window
        if server:
            print("Serving", APP_DIR, "at", url)
            try:
                while True:
                    time.sleep(3600)
            except KeyboardInterrupt:
                server.shutdown()
        return 0

    browser = find_browser()
    try:
        if browser:
            proc = open_window(browser, url)
            if already:
                return 0                                       # the first copy keeps the server running
            proc.wait()                                        # wait until you close the window
        else:
            webbrowser.open(url)                               # no Edge/Chrome found: use the normal browser
            if already:
                return 0
            say(APP_NAME, "Ink and Tales is open in your browser.\n\nClick OK when you are finished to close it.")
            if platform.system() != "Windows":
                while True:
                    time.sleep(3600)
    except KeyboardInterrupt:
        pass
    finally:
        if server:
            server.shutdown()
            server.server_close()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:                                  # never fail silently in the .exe
        log("ERROR " + repr(exc))
        say(APP_NAME, "Something went wrong:\n\n%s\n\nDetails are saved in %s" % (exc, os.path.join(data_dir(), "launcher.log")))
        sys.exit(1)
