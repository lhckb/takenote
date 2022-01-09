function hoverIn(id) {
    let div = document.getElementById(id)
    let actions = document.getElementById(`actions${id}`)

    div.style.backgroundColor = 'black'
    div.style.color = 'white' 

    actions.style.backgroundColor = 'white'
}

function hoverOut(id) {
    let div = document.getElementById(id)
    let actions = document.getElementById(`actions${id}`)

    div.style.backgroundColor = 'white'
    div.style.color = 'black' 
}

function deleteConfirmation(note_id) {
    if (window.confirm('Delete this note? You can\'t undo this.') == true) {
        window.location.href = `/notes/delete/${note_id}`
    }
    else {
        console.log('not')
    }
}

function enterUpdatePage(note_id) {
    window.location.href = `/notes/update/${note_id}/`
}

function redirectIndex() {
    window.location.href = '/'
}

function redirectNotes() {
    window.location.href = '/notes/'
}

function redirectUpdate(id) {
    window.location.href = `/notes/update/${id}`
}

function raiseAnchor() {
    let anchor = document.getElementById('headerAnchor')
    anchor.style.backgroundColor = 'white'
    anchor.style.color = 'black'
}

function lowerAnchor() {
    let anchor = document.getElementById('headerAnchor')
    anchor.style.backgroundColor = ''
    anchor.style.color = ''
}

function togglePin(id) {
    let note = document.getElementById(id)
    window.location.href = `/notes/togglepin/${id}`
}

function accountDelConfirmation(user) {
    if (window.confirm('Are you sure you want to delete your account? YOU CANNOT UNDO THIS')) {
        window.location.href = `/account/delete/${user}`
    }
}