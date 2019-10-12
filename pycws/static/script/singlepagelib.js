// Made this in order to simulate "single page application"

function getResponseBody(response) {
    return new Promise(function(resolve, reject) { 
        response.body.getReader().read().then(function(chunk) {
            resolve(new TextDecoder("utf-8").decode(chunk.value))
        })

    }) 
}

function getText(location) {
    // Get JSON for a location
    return new Promise(function(resolve, reject) {
        fetch(location).then(function(response) {
           if (response.ok) {
               console.log('OK')
               getResponseBody(response).then(text => resolve(text))
           } else {
               reject(response.status)
           }
           
        })
    })
}

function changeView(location) {
  refreshHeader()
  if(location == '#') {
    return
  }
  if (location == '') {
    return
  }
  $('#mainView').attr('src', location)
  window.history.pushState(location, '', '#' + location);
  $('#mainView')[0].refresh()
}

function refreshHeader() {
  $('header > x-frame')[0].refresh()

}

class ExternalIframe extends HTMLElement {
  constructor() {
    super()

    this.test = 'aa'
    this.refresh = function() {
      var e = this;
      e.innerText = 'Loading...';
      getText(this.getAttribute('src')).then(
          function(html) {
              e.innerHTML = html
          },
          function(error) {
              e.innerHTML = 'Error ' + error
          }
          
      )
    }

  }
}
    
window.customElements.define('x-frame', ExternalIframe)

class CwsLink extends HTMLElement {
  constructor() {
    super()
    this.onclick = function(e) {
      changeView(this.getAttribute('href'))
    }
  }
}

window.customElements.define('cws-link', CwsLink)

$().ready(function(a) {
  changeView(window.location.hash.substr(1))
})