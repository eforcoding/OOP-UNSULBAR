
package kalkulatorr;

import java.util.Scanner;

public class Kalkulatorr {

    
    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       int numbers1, numbers2, choice, result=0;
        System.out.println("KALKULATOR");
        System.out.println("1. penjumblahan");
        System.out.println("2. pengurangan");
        System.out.println("3. pembagian");
        System.out.println("4. perkalian");
        System.out.println("5. Sisa bagi");
        
        //input data
        
        System.out.println("input angka pertama");
        numbers1 = input.nextInt();
        System.out.println("input angka kedua");
        numbers2 = input.nextInt();
        
        //pilihan operasi
        System.out.println("Masukkan operasi");
        choice = input.nextInt();
        
        switch(choice)
        {
            case 1 : result = numbers1 + numbers2; break;
            case 2 : result = numbers1 - numbers2; break;
            case 3 : result = numbers1 / numbers2; break;
            case 4 : result = numbers1 * numbers2; break;
            case 5 : result = numbers1 % numbers2; break;
            default : System.out.println("pilihan salah");
            
            
        }
        System.out.println("Hasil: "+result);
       
    }

    private static void swich(int choice) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
    
}
