$(document).ready(function(){
    $(function() {

            $('#login-form-link').click(function(e) {
                $("#login-form").delay(100).fadeIn(100);
                $("#register-form").fadeOut(100);
                $('#register-form-link').removeClass('active');
                $(this).addClass('active');
                e.preventDefault();
            });
            $('#register-form-link').click(function(e) {
                $("#register-form").delay(100).fadeIn(100);
                $("#login-form").fadeOut(100);
                $('#login-form-link').removeClass('active');
                $(this).addClass('active');
                e.preventDefault();
            });
        });
});
$(document).ready(function(){

    $('#register-submit2').attr('disabled', true);

    $('input[name="reg_username"], input[name="reg_email"], input[name="reg_password"], input[name="reg_confirm_password"]').on('input', function() {
        var reg_usernameValue = $('#reg_username').val();
        var reg_emailValue = $('#reg_email').val();
        var reg_passwordValue = $('#reg_password').val();
        var reg_confirm_passwordValue = $('#reg_confirm_password').val();
        
        if (reg_usernameValue !== '' && reg_emailValue !== '' && reg_passwordValue !== '' && reg_confirm_passwordValue !== '') {

            var passRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
            if(!reg_passwordValue.match(passRegex)) {
                $('#reg_password_error').text('La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número').show();
                $('#register-submit2').attr('disabled', true);
            } else {
                $('#reg_password_error').hide();
         
                if (reg_confirm_passwordValue !== reg_passwordValue) {
                    $('#reg_confirm_password_error').text('Las contraseñas no coinciden').show();
                    $('#register-submit2').attr('disabled', true);
                } else {
                    $('#reg_confirm_password_error').hide();
                    $('#register-submit2').attr('disabled', false);
                    $('#form-menssage').hide();
                }
            }
        } else {
            $('#register-submit2').attr('disabled', true);
            $('#form-menssage').show();
        }

        var letters = /^[A-Za-z]+$/;
        if(!reg_usernameValue.match(letters)) {
            $('#reg_username_error').text('El nombre de usuario solo puede contener letras').show();
            $('#register-submit2').attr('disabled', true);
        } else {
            $('#reg_username_error').hide();
        }
    });
});
$(document).ready(function(){
    $('#register-submit2').click(function(e){
        e.preventDefault();
        window.location.href = "file:///C:/Users/Shunin/Documents/GitHub/Sumativa2/Sumativa2/core/templates/core/registro.html#";
    });
});