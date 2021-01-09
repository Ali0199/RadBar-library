function sendRequest(url, method, data) {
    var r = axios({
        method: method,
        url: url,
        data: data,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }

    })
    return r;

}
var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        books: [],
        a: 'Salom'

    },
    created() {
        var r = sendRequest('', 'get')
            .then(function(response) {
                this.books = response.data.book;
            })
    }
})