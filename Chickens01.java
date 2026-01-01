public class Chickens01 {
    public static void main(String[] args) {
        // First scenario: eggsPerChicken = 5, chickenCount = 3
        int eggsPerChicken1 = 5;
        int chickenCount1 = 3;
        int totalEggs1 = calculateTotalEggs(eggsPerChicken1, chickenCount1);
        System.out.println("Total eggs collected (scenario 1): " + totalEggs1);

        // Second scenario: eggsPerChicken = 4, chickenCount = 8
        int eggsPerChicken2 = 4;
        int chickenCount2 = 8;
        int totalEggs2 = calculateTotalEggs(eggsPerChicken2, chickenCount2);
        System.out.println("Total eggs collected (scenario 2): " + totalEggs2);
    }

    public static int calculateTotalEggs(int eggsPerChicken, int chickenCount) {
        // Monday
        int totalEggs = chickenCount * eggsPerChicken;

        // Tuesday: Increase chicken count by 1
        chickenCount += 1;
        totalEggs += chickenCount * eggsPerChicken;

        // Wednesday: Half the chickens are eaten by a wild beast
        chickenCount /= 2;
        totalEggs += chickenCount * eggsPerChicken;

        return totalEggs;
    }
}
