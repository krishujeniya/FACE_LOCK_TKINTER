
<a id="readme-top"></a>

![GitHub repo size](https://img.shields.io/github/repo-size/krishujeniya/FACE_LOCK_TKINTER)
![GitHub contributors](https://img.shields.io/github/contributors/krishujeniya/FACE_LOCK_TKINTER)
![GitHub stars](https://img.shields.io/github/stars/krishujeniya/FACE_LOCK_TKINTER?style=social)
![GitHub forks](https://img.shields.io/github/forks/krishujeniya/FACE_LOCK_TKINTER?style=social)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="logo.png" alt="Logo" width="80" height="80">

  <h1 align="center">FACE_LOCK_TKINTER</h1>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

FACE_LOCK_TKINTER is a graphical user interface (GUI) application developed using Python's Tkinter library. This application provides a facial recognition-based locking mechanism. The integration with Docker ensures a consistent environment for running the application.

### Key Features

- **User-Friendly Interface:**
  - Developed using Tkinter for a straightforward and intuitive interface.
  - Easy-to-use controls for a seamless experience.

- **Facial Recognition:**
  - Utilizes advanced facial recognition algorithms to authenticate users.
  - Ensures secure and efficient locking mechanism.

- **CustomTkinter Integration:**
  - Enhances UI elements with additional customization.

- **Docker Integration:**
  - Ensures a consistent and reproducible environment for running the application.

## Built With

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
- [![Tkinter](https://img.shields.io/badge/Tkinter-2C2255?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
- [![CustomTkinter](https://img.shields.io/badge/CustomTkinter-2C2255?style=for-the-badge&logo=python&logoColor=white)](https://github.com/TomSchimansky/CustomTkinter)
- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- **Python**: Ensure you have the latest version of Python installed. [Python Installation Guide](https://www.python.org/downloads/)
- **Docker**: Ensure you have the latest version of Docker installed. [Docker Installation Guide](https://docs.docker.com/get-docker/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/krishujeniya/FACE_LOCK_TKINTER.git
   cd FACE_LOCK_TKINTER
   ```

2. Build the Docker image
   ```sh
   docker build -t face_lock_tkinter .
   ```

3. Step-by-Step Guide to Enable X11 Forwarding in Docker

   **Install XQuartz (macOS) or Xming (Windows)**:
   - **macOS**: Install XQuartz from [XQuartz.org](https://www.xquartz.org/).
   - **Windows**: Install Xming from [Xming.org](https://sourceforge.net/projects/xming/).

   **Allow Connections**:
   - **macOS**: Open XQuartz, go to **Preferences > Security**, and check "Allow connections from network clients".
   - **Windows**: Start Xming with default settings.

   **Run Docker Container with X11 Forwarding**:

   **On Linux**:
   ```sh
   xhost +local:docker
   docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix face_lock_tkinter
   ```

   **On macOS with XQuartz**:
   ```sh
   xhost + 127.0.0.1
   docker run -it --rm -e DISPLAY=host.docker.internal:0 face_lock_tkinter
   ```

   **On Windows with Xming**:
   ```sh
   docker run -it --rm -e DISPLAY=host.docker.internal:0 face_lock_tkinter
   ```

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgments

* [Python](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* [Docker](https://www.docker.com/)
* [Open Source Community](https://opensource.org/)
* [Contributors](https://github.com/krishujeniya/FACE_LOCK_TKINTER/graphs/contributors)
