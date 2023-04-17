const form = document.getElementById("formulario-registro");
const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const fechaNacimiento = document.getElementById("fecha_nacimiento");
const password = document.getElementById("password");
const confirmarPassword = document.getElementById("confirmPassword");

form.addEventListener("submit", function(event) {
  event.preventDefault();
  checkInputs();
});

nombre.addEventListener("input", function() {
  checkNombre();
});

correo.addEventListener("input", function() {
  checkCorreo();
});

fechaNacimiento.addEventListener("input", function() {
  checkFechaNacimiento();
});

password.addEventListener("input", function() {
  checkPassword();
});

confirmarPassword.addEventListener("input", function() {
  checkConfirmarPassword();
});

function checkInputs() {
  checkNombre();
  checkCorreo();
  checkFechaNacimiento();
  checkPassword();
  checkConfirmarPassword();
}

function checkNombre() {
  const nombreValue = nombre.value.trim();

  if (nombreValue === "") {
    setErrorFor(nombre, "El nombre no puede estar vacío");
  } else {
    setSuccessFor(nombre);
  }
}

function checkCorreo() {
  const correoValue = correo.value.trim();

  if (correoValue === "") {
    setErrorFor(correo, "El correo electrónico no puede estar vacío");
  } else if (!isEmail(correoValue)) {
    setErrorFor(correo, "El correo electrónico no es válido");
  } else {
    setSuccessFor(correo);
  }
}

function checkFechaNacimiento() {
  const fechaNacimientoValue = fechaNacimiento.value.trim();

  if (fechaNacimientoValue === "") {
    setErrorFor(fechaNacimiento, "La fecha de nacimiento no puede estar vacía");
  } else {
    setSuccessFor(fechaNacimiento);
  }
}

function checkPassword() {
  const passwordValue = password.value.trim();

  if (passwordValue === "") {
    setErrorFor(password, "La contraseña no puede estar vacía");
  } else if (!isValidPassword(passwordValue)) {
    setErrorFor(password, "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, un número y un carácter especial");
  } else {
    setSuccessFor(password);
  }
}

function checkConfirmarPassword() {
  const confirmarPasswordValue = confirmarPassword.value.trim();
  const passwordValue = password.value.trim();

  if (confirmarPasswordValue === "") {
    setErrorFor(confirmarPassword, "Confirme la contraseña");
  } else if (passwordValue !== confirmarPasswordValue) {
    setErrorFor(confirmarPassword, "Las contraseñas no coinciden");
  } else {
    setSuccessFor(confirmarPassword);
  }
}

function setErrorFor(input, message) {
  const formControl = input.parentElement;
  const small = formControl.querySelector("small");
  formControl.classList.remove("success");
  formControl.classList.add("error");
  small.innerText = message;
}

function setSuccessFor(input) {
  const formControl = input.parentElement;
  formControl.classList.remove("error");
  formControl.classList.add("success");
}

function isEmail(email) {
  return /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email);
}

function isValidPassword(password) {
  const passwordRegex = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
  return passwordRegex.test(password);
}
