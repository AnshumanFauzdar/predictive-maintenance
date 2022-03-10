[![Video Demonstration](https://user-images.githubusercontent.com/40523329/151546529-868d12b0-08c2-4249-9135-29f47f4933a7.png)](https://youtu.be/ZZI74CT7vGE)

# Samvedan 2021 - TEAM MECHATRONICS

Documentation hosted on [sony.anshumanfauzdar.me](https://sony.anshumanfauzdar.me)

## Engineering guidelines to be followed:
**Guidelines to be followed for this project:**

- **KISS -** Keep it stupid simple.
- No extra features until and unless it is a bug.
- Revisit official documentation in case of no results found on google or forums.
- Create safe fallback features and try to re-create until and unless it is a bug.
- In case of creative block discuss with team ASAP.

**Promised Features:**

- Camera Monitoring - Images only
- Microphone - noise detection
- WiFi connectivity - ESP8266/32
---
For predictive maintenance:
- Temperature sensor - real time data
- Speakers - for notifications
- HMI - for displaying data
- Modular structure - 3D printed + aluminum extrusion structure
- Server - cloud implementation

## Development lifecycle
All the software, CAD, electronics development will be done with git and uploaded here to GitHub

1. Create a branch off of master:

Only in case of working on new feature not aligned with master branch.
Name the branch with your first name pre-pended [do not create unnecessary branches]:
spresense/cool-feature

2. Writing Code:

GitHub upload instructions:

- Standard PR should be made to merge features with log including changes and bug fixes.
- To make standard changes follow engineering guidelines.
- For making revision of CAD models mention version ex. Mount_v2.0.1

3. Submit for review:

- Assign the task to the appropriate reviewer.
- Once tested and approved from all team members PR will be merged.

## Software Architecture
```mermaid
  graph TD;
    A[Start Software] --> B{{Check Internet Connection}};
    B --> C(connected to internet);
    B --> E(Not connected to internet);
    C --> D(update to latest dataset and firmware);
    E --> F(use local dataset and firmware edgeML);
    D --> G;
    F --> G{{Data acquisition from camera and microphone/vibration/temperature sensors}};
    G --> H(Image/video data in realtime)
    G --> I(Microphone/vibration/temperature sensor real time data)
    H --> J(Monitoring with ML and AI on Edge)
    I --> K(Monitoring with noise filtering and AI/ML on the edge)
    J --> L;
    K --> L{{Leakage, excess, noise/vibration, wrong part handling, heat etc. detected}}
    L -->|YES| M{{Notify nearest production line worker and visual/audio notifications}}
    M -->|Yes| N[\Action Taken\]
    M -->|No| O[\No action taken after certain time\]
    O --> P{{MACHINE AUTO TURN OFF and notify all}}
    P --> Q[\Acquire data and improve detection dataset\]
    Q --> R[Repeat Process]
    N --> R
```

## Road Map
- [ ]  [⚠️ VERY IMPORTANT ⚠️] **Burning Bootloader**
- [ ]  [⚠️ VERY IMPORTANT ⚠️] Setting up camera
- [ ]  Wi-Fi Connection - ESP8266
- [ ]  Try Examples - Wi-Fi functionality only
- [ ]  Try multicore functionality
- [ ]  Attach microphone and temperature sensors
- [ ]  Deploy to edge impulse
- [ ]  Initial image detection
- [ ]  Noise detection
- [ ]  Temperature variation detection
- [ ]  Mix all the detection in single application
- [ ]  Make webserver to show all data
