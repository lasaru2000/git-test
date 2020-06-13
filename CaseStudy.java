import java.text.DecimalFormat;
import java.util.Scanner;

public class CaseStudy {
    public static void main(String[] args) {
        Scanner sn=new Scanner(System.in);

        //Ger Inputs
        System.out.print("Enter weight in pounds: ");
        double weight = sn.nextDouble();
        System.out.print("Enter height in inches: ");
        double height = sn.nextDouble();
        //Output format (Decimal Numbers)
        DecimalFormat decimalFormat = new DecimalFormat("##.00");


        //Calculate BMI
        double BMI=(weight * 0.45359237)/Math.pow(height * 0.0254,2);
        System.out.println("BMI is "+ decimalFormat.format(BMI));

        //Interpretation of BMI
        if(BMI>=30){
            System.out.println("Obese");
        }
        else if(BMI>=25){
            System.out.println("Over Weight");
        }
        else if(BMI>=18.5){
            System.out.println("Normal");
        }
        else{
            System.out.println("Under Weight");
        }

    }
}
