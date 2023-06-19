 const API_URL = 'https://testservices.wschilexpress.com';

const xhr = new XMLHttpRequest();


function onRequestHandler() {
    if (this.readyState === 4 && this.status === 200){
        // 0 = unset
        // 1 opened
        // 2 headers_recieved
        // 3 loading
        // 4 done
        console.log(this.response);

    }
}

xhr.addEventListener("load", onRequestHandler);
xhr.open("GET", '${API_URL}/body');
xhr.send();