function opencvReady() {
    cv["onRuntimeInitialized"] = () => {
        console.log('OpenCV Ready')

        let maining = cv.imread("viz-img")
        cv.imshow("viz-canvas", maining)
        maining.delete()
    }
}