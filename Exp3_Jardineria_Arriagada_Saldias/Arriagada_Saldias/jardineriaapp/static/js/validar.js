//Creacion cuenta
$(function(){
    $("#crear-cuenta").validate({
        rules:{
            nom:{
                required:true
            },
            apellido:{
                required:true,
            },
            correo:{
                required:true,
                email:true
            },
            pass1:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:pass1
            },
        },//rules
        messages:{
            nom:{
                required:'Ingrese un nombre de usuario',
                minlegth:'formato incorrecto de nombre (3)'
            },
            apellido:{
                    required:'Ingrese su apellido',
                    minlegth:'formato incorrecto de apellido(3)'
            },
            correo:{
                required:'Ingreso su correo',
                email: 'Formato de correo invalido'
            },
            pass1:{
                required:'Ingrese su Contraseña',
                minlegth:'Caracteristicas insuficientes'
            },
            pass2:{
                required:'Ingrese su contraseña anterior',
                minlegth: 'Caracteristicas insuficientes(8)',
                equalTo: 'Contraseñas no coinciden'
            },

            
        },//messages
    })
});








