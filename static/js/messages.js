let loc =window.location
let wsStart = 'ws://'


if(location.protocol=='https'){
    wsStart='wss://'
}
let endpoint = wsStart + loc.host + location.pathname

var socket= new WebSocket(endpoint)

socket.onopen= async function(e){
    console.log('open',e)
}
socket.onmessage= async function(e){
    console.log('message',e)
}
socket.onerror= async function(e){
    console.log('error',e)
}
socket.onclose= async function(e){
    console.log('close',e)
}

// let url ='ws://${window.location.host}/ws/socket-server/'
// const chatsocket= new
socket.onmessage=function (e){
    let data= JSON.parse(e.data)
    console.log('Data:',data)
}
