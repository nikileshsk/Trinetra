document.addEventListener('DOMContentLoaded', function() {
    var checkButton = document.getElementById('checkButton');

    checkButton.addEventListener('click', function() {
        var urlInput = document.getElementById('urlInput').value;
        if (urlInput.trim() === '') {
            alert('Please enter a URL');
            return;
        }

        // Send a message to background script to initiate URL check
        chrome.runtime.sendMessage({action: 'checkURL', url: urlInput}, function(response) {
            var resultDiv = document.getElementById('result');
            resultDiv.innerText = response;
        });
    });
});
