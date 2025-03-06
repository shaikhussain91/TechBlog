function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    if (!email || !password) {
        alert('Please fill in all fields');
        return redirect('myapp:main');
    }
   
}
function createAccount() {
    alert('Redirecting to account creation...');
    // Add create account functionality here
}
function createAccount() {
    // Redirect to the Create Account page
    window.location.href = '/create-account/';
}
