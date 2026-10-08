\# FieldVision – AI-Powered Football Video Analysis



FieldVision is a computer vision-based football analysis system that processes football match videos to detect, track, and analyze players and the ball.



The project uses \*\*YOLOv8n\*\* for object detection and combines multiple computer vision techniques to provide player tracking, team assignment, ball possession analysis, camera movement estimation, perspective transformation, player speed, and distance measurements.



\---



\## Project Overview



The system takes a football match video as input and processes each frame to identify important objects on the field.



The detected objects are tracked throughout the video, allowing the system to perform higher-level football analytics such as:



\- Player detection and tracking

\- Ball detection and tracking

\- Player identification using tracking IDs

\- Team assignment

\- Ball possession analysis

\- Camera movement estimation

\- Perspective transformation

\- Player speed estimation

\- Distance covered by players



\---



\## Key Features



\### 1. Player Detection



Players are detected in each frame using the YOLOv8n object detection model.



Each detected player is assigned a bounding box and tracking ID so that the same player can be followed across multiple frames.



\### 2. Ball Detection



The football is detected and tracked throughout the match video.



The detected ball position is used for further analysis such as ball possession.



\### 3. Player Tracking



A tracking system maintains the identity of detected players across video frames.



This allows the system to calculate player movement and analyze individual player performance.



\### 4. Team Assignment



Players are assigned to teams based on the visual characteristics of their appearance.



The team assignment is then displayed on the processed video.



\### 5. Ball Possession



The system determines which player is closest to the ball and uses this information to estimate ball possession.



This provides an overview of which team/player controls the ball during different parts of the match.



\### 6. Camera Movement Estimation



Football cameras continuously move during a match.



The project estimates camera movement so that player movement can be analyzed more accurately despite changes in the camera position.



\### 7. Perspective Transformation



A perspective transformation is applied to convert the camera view into a more representative top-down/bird's-eye view of the football field.



This helps in estimating player movement on the field.



\### 8. Player Speed Estimation



Using player tracking information, perspective transformation, and frame timing, the system estimates the speed of players during the match.



\### 9. Distance Covered



The movement of each tracked player is used to estimate the distance covered by the player during the analyzed video.



\---



\## Technology Stack



\- Python

\- OpenCV

\- YOLOv8

\- Ultralytics

\- NumPy

\- Pandas

\- Matplotlib

\- Seaborn

\- Roboflow

\- Jupyter Notebook



\---



\## Object Detection Model



The project uses:



\*\*YOLOv8n\*\*



YOLOv8n is the nano version of the YOLOv8 object detection model and was selected for this project because it provides a lightweight and efficient solution for real-time object detection.



The model is used to detect football-related objects in the video.



\---



\## Dataset



The object detection model uses a football player detection dataset obtained from \*\*Roboflow Universe\*\*.



\### Dataset Information



| Property | Details |

|---|---|

| Dataset | Football Players Detection |

| Dataset ID | `football-players-detection-3zvbc` |

| Version | Version 1 |

| Source | Roboflow Universe |

| Download Format | YOLOv5 |

| Number of Images | 372 |

| Classes | 4 |



\### Classes



The dataset contains the following object classes:



\- `player`

\- `goalkeeper`

\- `referee`

\- `ball`



The dataset was downloaded from Roboflow in YOLO format and used for the football object detection component of the project.



\### Dataset Source



\[Football Players Detection Dataset – Roboflow Universe](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc)



\---



\## Dataset Download



The dataset was accessed using the Roboflow Python API.



The API key is intentionally \*\*not included\*\* in this repository for security reasons.



Example:



```python

from roboflow import Roboflow



rf = Roboflow(api\_key="YOUR\_ROBOFLOW\_API\_KEY")



project = rf.workspace("roboflow-jvuqo").project(

&#x20;   "football-players-detection-3zvbc"

)



version = project.version(1)



dataset = version.download("yolov5")







Project Workflow:



Input Football Video

&#x20;       |

&#x20;       v

Object Detection using YOLOv8n

&#x20;       |

&#x20;       v

Player / Ball / Referee / Goalkeeper Detection

&#x20;       |

&#x20;       v

Object Tracking

&#x20;       |

&#x20;       +--------------------+

&#x20;       |                    |

&#x20;       v                    v

&#x20;Team Assignment       Ball Tracking

&#x20;       |                    |

&#x20;       +---------+----------+

&#x20;                 |

&#x20;                 v

&#x20;         Ball Possession

&#x20;                 |

&#x20;                 v

&#x20;      Camera Movement Estimation

&#x20;                 |

&#x20;                 v

&#x20;       Perspective Transformation

&#x20;                 |

&#x20;                 v

&#x20;      Player Movement Analysis

&#x20;                 |

&#x20;         +-------+-------+

&#x20;         |               |

&#x20;         v               v

&#x20;   Player Speed     Distance Covered

&#x20;         |               |

&#x20;         +-------+-------+

&#x20;                 |

&#x20;                 v

&#x20;          Output Video





Commands to run:

git clone https://github.com/Monisha0685/Projects.git

cd Projects/FieldVision



python -m venv fieldvision

fieldvision\\Scripts\\activate



pip install -r requirements.txt



python main.py

