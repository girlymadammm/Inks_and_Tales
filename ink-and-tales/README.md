# Ink & Tales
A writing studio for stories, journals and ideas. **Made by Ashki Studio.** *Ideas into experiences.*

This folder is the whole app. It runs in any modern browser and can be installed like a normal app
on Windows, Android, iPhone/iPad, Mac, Linux and Chromebook. It works offline after the first visit.

## What is in this folder
| File | What it does |
|---|---|
| `index.html` | The app itself (stories, journal, pin board, music, export, everything) |
| `manifest.webmanifest` | Tells phones and laptops the app's name, colors and icon so it can be installed |
| `sw.js` | Makes the app work offline |
| `icons/` | Your Ashki Studio feather icon in the sizes devices need |
| `LICENSE` | "All rights reserved" notice for Ashki Studio |

## Put it on GitHub (account: Girlymadammm)
1. Sign in at github.com and click **New** (new repository).
2. Name it `ink-and-tales`, choose **Public**, leave the other boxes empty, click **Create repository**.
3. Click **uploading an existing file**. Open this folder on your computer and drag **everything inside it**
   (`index.html`, `manifest.webmanifest`, `sw.js`, `LICENSE`, and the `icons` folder) into the page.
   Wait until all files finish uploading, then click **Commit changes**.
4. Go to **Settings, then Pages**. Under *Build and deployment*, set **Source** to *Deploy from a branch*,
   **Branch** to `main` and the folder to `/ (root)`. Click **Save**.
5. Wait one or two minutes and refresh. GitHub shows your link, which will look like
   **https://girlymadammm.github.io/ink-and-tales/**

If the `icons` folder does not upload, open the folder, select the five pictures, and upload them again
after clicking **Add file, then Upload files**. Then create the folder by dragging them in under the name `icons`.

## Install it
- **Windows:** open the link in **Edge** or **Chrome**. Click the install icon at the right end of the address bar
  (or the three dots, then *Apps*, then *Install this site as an app*). It gets its own window and a Start menu icon.
- **Android:** open the link in **Chrome**, tap the three dots, then **Install app** (or **Add to Home screen**).
- **iPhone / iPad:** open the link in **Safari**, tap **Share**, then **Add to Home Screen**.
  Start writing from the new icon, not from Safari. The installed app keeps its own separate storage.
- **Mac, Linux, Chromebook:** open the link in Chrome or Edge and use the install icon in the address bar.

Send your sister the same link. Each person's stories stay on their own device and are private to them.

## Keep your writing safe
Stories are saved inside the browser on each device. They do not sync between devices and they are removed
if someone clears the browser's data. In the app, go to **Settings, then Your data, then Save backup**
now and then. To move to a new device, open the app there and choose **Restore backup**.
Browsers also allow only about 5 MB of saved data, and pictures use it quickly. The app shows how much you have used
and warns you in red if it is full.

## Updating the app later
1. Replace `index.html` on GitHub (open the file, click the pencil or **Add file, Upload files**, and commit).
2. Open `sw.js`, change `const VERSION = 'v1';` to `'v2'` (then `'v3'` and so on), and commit.
3. Devices pick up the new version the next time the app is opened (sometimes after opening it twice).

## Credits
Ink & Tales is made by **Ashki Studio** (GitHub: Girlymadammm). Fonts come from Google Fonts (open-source licenses).
The soundscapes are original loops from the Ink & Tales audio collection.
