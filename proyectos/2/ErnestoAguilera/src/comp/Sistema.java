/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package comp;

/**
 * @version 0.1
 * @author Luis
 */
public class Sistema {
    private static float tiempoSistema;

    public static void main(String[] args){
        
    }
    
    public static synchronized float getTiempoSistema() {
        return tiempoSistema;
    }

}
