# Gesture to LLM - Rule-based Sign Language Detection

A simple hobby project that detects hand gestures using MediaPipe and sends text to an LLM via webhook.

## Features

- Real-time hand gesture detection using MediaPipe
- 5 basic gestures: Thumbs Up, Thumbs Down, Open Palm, Fist, Pointing
- Automatic text buffering with configurable timeout
- Sends text to webhook endpoint for LLM processing
- Visual feedback with hand landmarks and gesture recognition
- Scrolling ticker for LLM responses
- Threaded webhook requests to prevent UI freezing
- Configurable gesture cooldown to prevent duplicate detections

## Prerequisites

- Python 3.8 or higher
- A webcam/camera for gesture detection
- Access to a webhook endpoint that accepts text input and returns LLM responses

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd gesture-llm
```

2. Download the MediaPipe hand landmark model:
   - Download the `hand_landmarker.task` file from the [MediaPipe Models](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker#models) page
   - Place it in the project root directory

3. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file with your configuration (see `.env.example` for reference)

6. Run:
```bash
python main.py
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
WEBHOOK_URL=https://your-webhook-endpoint.com/webhook
SESSION_ID=session_001
TIMEOUT_SECONDS=4.0
CONFIDENCE_THRESHOLD=0.7
GESTURE_COOLDOWN_SECONDS=2.5
```

See the `.env.example` file for detailed descriptions of each variable.

## Gesture Mappings

| Gesture | Word |
|----------|-------|
| Thumbs up | yes |
| Thumbs down | no |
| Open palm | hello |
| Fist | stop |
| Pointing | what |

You can customize these mappings in `config.py`.

## Usage

- Position yourself in front of the camera
- Show gestures to camera - recognized gestures will be displayed
- Words buffer automatically as you make gestures
- After the configured timeout period of inactivity, the sentence is sent to the LLM
- LLM response scrolls across the top of the screen
- Press 'q' to quit the application

## Configuration Options

The following configuration options can be set in the `.env` file:

- `WEBHOOK_URL`: The URL of your webhook endpoint that handles the text input and returns LLM responses
- `SESSION_ID`: Session identifier to maintain conversation context (optional)
- `TIMEOUT_SECONDS`: Time in seconds to wait before sending the buffered text (default: 4.0)
- `CONFIDENCE_THRESHOLD`: Minimum confidence threshold for gesture detection (default: 0.7)
- `GESTURE_COOLDOWN_SECONDS`: Minimum time between identical gesture detections (default: 2.5)

## Project Structure

```
gesture-llm/
├── main.py                 # Main application entry point
├── config.py               # Configuration and environment variables
├── hand_landmarker.task    # MediaPipe hand landmark model file
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .env.example           # Example environment variables file
├── models/                # Model files (if any)
└── src/                   # Source code modules
    ├── __init__.py
    ├── camera.py          # Camera interface
    ├── display.py         # Display and visualization
    ├── gesture_detector.py # Gesture detection logic
    ├── text_buffer.py     # Text buffering system
    └── webhook_client.py  # Webhook communication
```

## How It Works

1. **Camera Module**: Captures frames from the default camera
2. **Gesture Detector**: Uses MediaPipe to detect hand landmarks and classify gestures
3. **Text Buffer**: Collects detected words and holds them until timeout
4. **Webhook Client**: Sends collected text to the configured webhook endpoint
5. **Display Module**: Shows camera feed with overlays for gestures, buffer, and LLM responses
6. **Threading**: Webhook requests run in a separate thread to prevent UI freezing

## Customization

### Adding New Gestures

1. Modify the gesture detection logic in `src/gesture_detector.py`
2. Add the new gesture to the `GESTURE_MAP` in `config.py`

### Changing Gesture Mappings

Modify the `GESTURE_MAP` dictionary in `config.py` to map gestures to different words.

### Adjusting Sensitivity

Adjust the `CONFIDENCE_THRESHOLD` in the environment variables to change detection sensitivity.

## Troubleshooting

- If you see an error about `hand_landmarker.task` not being found, ensure you've downloaded the model file and placed it in the project root
- If gestures aren't being detected, try adjusting the lighting conditions or the camera angle
- If the application is slow, ensure you have sufficient CPU resources available
- Check that your webhook endpoint is accessible and properly configured

## Dependencies

- opencv-python: For camera capture and image processing
- mediapipe: For hand landmark detection
- requests: For webhook communication
- numpy: For numerical computations
- python-dotenv: For environment variable management
