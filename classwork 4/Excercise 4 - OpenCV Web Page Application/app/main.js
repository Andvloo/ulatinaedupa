function opencvReady() {
    cv["onRuntimeInitialized"] = () => {
        console.log('OpenCV Ready') // log to the console to validate opencv

        document.getElementById("button-rgb").onclick = function () {
            video.pause()
            let mainimg = cv.imread("viz-img"); // read the image
            cv.imshow("viz-canvas", mainimg); // display in canvas
            mainimg.delete(); // release memory    
        };

        document.getElementById("button-gray").onclick = function () {
            let mainimg = cv.imread("viz-img"); // read the image
            let imggray = mainimg.clone(); // placeholder for gray image
            cv.cvtColor(mainimg, imggray, cv.COLOR_RGBA2GRAY, 0); // conver the image to gray
            cv.imshow("viz-canvas", imggray); // display in canvas
            mainimg.delete(); // release memory
            imggray.delete(); // release memory
        };

        document.getElementById("button-blur").onclick = function () {
            let mainimg = cv.imread("viz-img"); // read the image
            let imgblur = mainimg.clone(); // image blurring
            let ksize = new cv.Size(15,15); // kernel size
            cv.GaussianBlur(mainimg, imgblur, ksize, 0);  // gaussian blur
            cv.imshow("viz-canvas", imgblur); // display in canvas
            mainimg.delete(); // release memory
            imgblur.delete(); // release memory
        };

        document.getElementById("button-canny").onclick = function () {
            let mainimg = cv.imread("viz-img"); // read the image
            let imgcanny = mainimg.clone();
            cv.Canny(mainimg, imgcanny, 50, 100)    
            cv.imshow("viz-canvas", imgcanny); // display in canvas
            mainimg.delete(); // release memory
            imgcanny.delete(); // release memory
        }; 
    }
}






let video = document.getElementById("viz-video"); // video is the id of video tag
navigator.mediaDevices
  .getUserMedia({ video: true, audio: false })
  .then(function(stream) {
    video.srcObject = stream;
    video.play();

    let src = new cv.Mat(video.height, video.width, cv.CV_8UC4);
    let dst = new cv.Mat(video.height, video.width, cv.CV_8UC1);
    let cap = new cv.VideoCapture(video);

    const FPS = 30;
    function processVideo() {
      try {
        // if (!streaming) {
        //   // clean and stop.
        //   src.delete();
        //   dst.delete();
        //   return;
        // }
        let begin = Date.now();
        // start processing.
        cap.read(src);
        cv.cvtColor(src, dst, cv.COLOR_RGBA2GRAY);
        cv.imshow("viz-canvas", dst);
        // schedule the next one.
        let delay = 1000 / FPS - (Date.now() - begin);
        setTimeout(processVideo, delay);
      } catch (err) {
        console.error(err);
      }
    }

    // schedule the first one.
    setTimeout(processVideo, 0);
  })
  .catch(function(err) {
    console.log("An error occurred! " + err);
  });
