## Machine Learning Operations(MLOps)

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

While there are many projects that on Machine learning models, we usually do not have many on setting up the environment to allow easier and faster deployment of these models. This project offers developers working on YoloV5 for object detection a setup environment to test and deploy their applications. How?

By offering the following:

- A flask application to utilize your Yolo Model and return prediction
- Integration with Dockerhub for hosting the contenerized application
- A configured connection with AWS EC2 instance, allowing automatic deployment upon push to the main branch or a pull request from other brances
- A logging and monitoring capability for incoming and outgoing requests on AWS CloudWatch

Of course, no one pipeline would serve all the needs of different ML engineers. I will be adding more use cases to allow more developers to easily deploy and test their models in the AWS enviroment..

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

The following gives you instructions on how you might setup this enviroment locally to allow further testing the system or develop further on the concepts of this repository.

### Prerequisites

You will need Python 3.8 or above to run this project. It is recommended that you run this in a virtual enviroment, you can create the virtual environment using the following commands.

- python
  ```sh
  python3 -m venv myenv
  virtualenv myenv
  source myenv/bin/activate
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/Basi10/Yolo-MicroService-Deployment.git
   ```
2. Install python packages
   ```sh
   pip install requirements.txt
   ```
3. Install the AWS cli if you want to make adjustments to it

   You can follow the steps in this link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

After cloning the repository, there are two ways you can interact with the current application

### Docker

1. Build the docker image
   ```sh
   docker build -t my_image_name:tag_name .
   ```
2. Run the image in your local environment
   ```sh
   docker run -p 8000:8000 my_image_name:tag_name
   ```

### Python

You have to install the dependencies as well in the installation process.

1. Navigate to the project root directory
   ```sh
   cd Yolo-MicroService-Deployment
   ```
2. Run the flask application
   ```sh
   python app.py
   ```

You can interact with the running application on localhost mapped to the port 8000. The '/infer' endpoint can be utilized to detect objects from an image URL. You can send the command in the following format:

```sh
{
 "image_url": "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGhvdG98ZW58MHx8MHx8fDA%3D"
 }

```

The response will be in json format consisting of the detected objects and the corresponding confidence score.

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Basilel Birru - basilelbirru@gmail.com

Project Link: [https://github.com/Basi10/Yolo-MicroService-Deployment.git](https://github.com/Basi10/Yolo-MicroService-Deployment.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
