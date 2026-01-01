/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package week4.java;

import java.util.Random;
/**
 *
 * @author user
 */
public class Week4Java {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Random rand = new Random();
        int sum;
        int week1 = rand.nextInt(6) +1;
        int week2 = rand.nextInt(6) +1;
        sum = week1 + week2 ; 
        System.out.println(week1 + " + " + week2 + " = " +sum );
        // TODO code application logic here
    }
    
}
