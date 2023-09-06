import { Component, OnInit } from '@angular/core';
import { MenuController } from '@ionic/angular';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-registrar',
  templateUrl: './registrar.page.html',
  styleUrls: ['./registrar.page.scss'],
})
export class RegistrarPage implements OnInit {
      
  usuario={
    nombre:'',
    email:'',
    password:''

  }
  constructor(private menuController : MenuController,
              private alertController: AlertController ) { }

  ngOnInit() {
  }
  MostrarMenu(){
   this.menuController.open('first');
  }

  async Enviar(){
    const alert = await this.alertController.create({
      header: 'Gracias!' + ' '+ this.usuario.nombre,
      message: 'Se Ha registrado Correctamente',
      buttons: ['OK'],
    });

    await alert.present();
    this.usuario.nombre='';
    this.usuario.email='';
    this.usuario.password='';
  }
}
