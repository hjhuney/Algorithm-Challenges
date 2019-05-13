// HORSE algorithm
// Keeps score for game of H-O-R-S-E in basketball

using System;

class MainClass {
  public static void Main (string[] args) {
    
    string test1 = "miss miss hit miss hit miss hit miss miss hit miss miss miss miss hit hit hit miss hit miss";

    string[] shots = test1.Split(' ');
    string horse = "HORSE";

    int counter = 0;
    int p1_misses = 0;
    int p2_misses = 0;


    while(counter < shots.Length) {
      if(shots[counter] == "hit") {
        if(shots[counter+1] == "miss") {
          if((counter+1) %2 == 0) {
            p1_misses = p1_misses + 1;
          }
          else {
            p2_misses = p2_misses + 1;
          }
        }
        counter = counter + 2;
      }
      else {
        counter = counter + 1;
      }
    }

    if(p1_misses == 0) {
      Console.WriteLine("Player 1: ");
    } else if (p1_misses > 5) {
      Console.WriteLine("Player 1: HORSE");
    } else {
      Console.WriteLine("Player 1: " + horse.Substring(0, p1_misses));
    }

    if(p2_misses == 0) {
      Console.WriteLine("Player 2: ");
    } else if (p2_misses > 5) {
      Console.WriteLine("Player 2: HORSE");
    } else {
      Console.WriteLine("Player 2: " + horse.Substring(0, p2_misses));
    }
  }
}