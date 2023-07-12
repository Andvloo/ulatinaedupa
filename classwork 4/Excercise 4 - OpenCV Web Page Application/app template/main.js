function opencvReady() {
    cv["onRuntimeInitialized"] = () => {
        console.log('OpenCV Ready') // log to the console to validate opencv

        let mainimg = cv.imread("viz-img") // read the image
        cv.imshow("viz-canvas", mainimg) // display in canvas
        mainimg.delete() // release memory
    }
}