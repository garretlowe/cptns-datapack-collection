import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class ChangeRate {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter new wait time (ticks): ");
        int val = sc.nextInt();
        sc.close();
        System.out.println();

        String output = "scoreboard players add ticks path_randomizer 1" + System.lineSeparator()
                + "execute if score ticks path_randomizer matches %d.. run scoreboard players set ticks path_randomizer 0 "
                + System.lineSeparator()
                + "execute if score ticks path_randomizer matches 0 run function cptnjtk:check_air";

        File file = new File("./data/cptnjtk/functions/main.mcfunction");
        try {
            FileWriter fw = new FileWriter(file, false);
            fw.write(String.format(output, val + 1));
            fw.close();
            System.out.println("Wait time successfully changed.");
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("An error occurred. Wait time may not have been changed.");
        }
    }
}