// static/list_sessions.js
document.addEventListener('DOMContentLoaded', () => {
    console.log("list_sessions.js loaded");

    const usernameInput = document.getElementById('username');
    const newSessionForm = document.querySelector('.new-session-form form');

    if (usernameInput) {
        usernameInput.focus();
    }

    if (newSessionForm) {
        newSessionForm.addEventListener('submit', (event) => {
            if (usernameInput && usernameInput.value.trim() === '') {
                alert('Vui lòng nhập tên của bạn.');
                event.preventDefault(); 
            }
           
        });
    }

}); 