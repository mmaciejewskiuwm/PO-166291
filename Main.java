import javax.lang.model.type.NullType;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner n = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Podaj N");
        int wart = n.nextInt();
        System.out.println(wart);
        double[] tab;
        tab = new double[wart];
        for (int i = 0; i < wart; i++) {
            System.out.println(" Podaj wartosc ");
            Scanner x = new Scanner(System.in);
            double p = x.nextInt();
            tab[i] = p;
        }
        // A
        double zada = 0;
        for (int i = 0; i < wart; i++) {
            zada = zada + tab[i];

        }
        System.out.println("Podpunkt a dla tych liczb");
        System.out.println(zada);
        // B
        double zadb = 1;
        for (int i = 0; i < wart; i++) {
            zadb = zadb * tab[i];

        }
        System.out.println("Podpunkt b dla tych liczb");
        System.out.println(zadb);
        // C

        double zadc = 0;
        for (int i = 0; i < wart; i++) {
            zadc = zadc + Math.abs(tab[i]);

        }
        System.out.println("Podpunkt c dla tych liczb");
        System.out.println(zadc);
        //D
        double zadd = 0;
        for (int i = 0; i < wart; i++) {
            zadd = (zadd + Math.sqrt(Math.abs(tab[i])));

        }
        System.out.println("Podpunkt d dla tych liczb");
        System.out.println(zadd);
        // E

        double zade = 1;
        for (int i = 0; i < wart; i++) {
            zade = zade * Math.abs(tab[i]);

        }
        System.out.println("Podpunkt e dla tych liczb");
        System.out.println(zade);
        // F
        double zadf = 0;
        for (int i = 0; i < wart; i++) {
            zadf = (int) (zadf + Math.pow(tab[i], 2));

        }
        System.out.println("Podpunkt f dla tych liczb");
        System.out.println(zadf);
        // G
        double zadg1 = 0;
        double zadg2 = 1;
        for (int i = 0; i < wart; i++) {
            zadg1 = zadg1 + tab[i];
            zadg2 = zadg2 * tab[i];

        }
        System.out.println("Podpunkt g dla tych liczb");
        System.out.println(zadg1 + " oraz " + zadg2);
        //H
        double zadh = 0;
        for (int i = 0; i < wart; i++) {
            if(i == wart-2)
            {
                zadh = zadh + Math.pow(-1,i);
            } else if (i == wart-1) {
                zadh = zadh * tab[i];
            } else if (i % 2 ==0) {
                zadh = zadh + tab[i];
            } else{
                zadh = zadh - tab[i];
            }


        }
        System.out.println("Podpunkt h dla tych liczb");
        System.out.println(zadh);
    }
}