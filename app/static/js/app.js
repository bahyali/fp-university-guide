function Search() {
    let search_bar = document.querySelector("#search");
    let results_list = document.querySelector("#search-results")

    if (!search_bar || !results_list)
        return

    let url = "/api/search?query="
    let timeout = undefined

    function render(response) {
        let results = ""
        for (let i = 0; i < response.length; i++) {
            results += `<li>${response[i].name}</li>`
        }
        results_list.innerHTML = results
    }

    function call_api(query) {
        fetch(url + query)
            .then(res => res.json())
            .then(function (response) {
                console.log('response', response)
                render(response)
            }, function (error) {
                console.error('error', error)
            })
    }

    function createTimeout() {
        return setTimeout(function () {
            call_api(search_bar.value)
        }, 333)
    }

    search_bar.addEventListener('input', function () {
        // debounce
        if (timeout) {
            clearTimeout(timeout)
        }
        timeout = createTimeout()
    })
}

(function init() {
    Search()
})()