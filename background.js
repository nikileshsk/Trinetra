chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    console.log("Received message from popup:", request);
    if (request.action === 'checkURL') {
        var url = request.url;
        console.log("URL to check:", url);
        // Simulate a response for testing purposes
        var result = "Test result: URL is safe";
        sendResponse(result);
    }
});
