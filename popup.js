document.addEventListener('DOMContentLoaded', function () {
    const passwordLengthInput = document.getElementById('passwordLength');
    const passwordLengthValue = document.getElementById('passwordLengthValue');
    const generatePasswordButton = document.getElementById('generatePassword');
    const copyPasswordButton = document.getElementById('copyPassword');
    const passwordResult = document.getElementById('passwordResult');
  
    function generateRandomPassword(length) {
      const charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=';
      let password = '';
      for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset.charAt(randomIndex);
      }
      return password;
    }
  
    passwordLengthInput.addEventListener('input', function () {
      passwordLengthValue.textContent = passwordLengthInput.value;
    });
  
    generatePasswordButton.addEventListener('click', function () {
      const length = parseInt(passwordLengthInput.value);
      const newPassword = generateRandomPassword(length);
      passwordResult.textContent = newPassword;
    });
  
    copyPasswordButton.addEventListener('click', function () {
      const newPassword = passwordResult.textContent;
      navigator.clipboard.writeText(newPassword).then(function () {
        alert('Password copied to clipboard.');
      });
    });
  });
  