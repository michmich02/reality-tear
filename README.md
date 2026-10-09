# Reality Tear

> Split and distort a live scene with your hands.

[**View live demo →**](https://michmich02.github.io/reality-tear/)

## Overview

Reality Tear is a spatial interaction experiment where gestures appear to pull apart the camera image itself. The project focuses on dramatic feedback, depth, and the feeling of manipulating a digital surface directly.

## Interaction

- Allow camera access.
- Keep your hands visible in good lighting.
- Use the prompted gesture to open and control the tear.

## Built with

`JavaScript` · `Three.js` · `WebGL` · `MediaPipe`

## Run locally

```sh
python3 -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000) in a desktop browser. Camera and microphone APIs require localhost or HTTPS; external models and CDN dependencies require an internet connection.

## Design notes

- Immediate visual feedback keeps the gesture-to-effect relationship legible.
- The experience is designed as a focused, full-screen interaction.
- Processing happens in the browser; camera and microphone streams are not uploaded by this project.
