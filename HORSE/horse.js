// algorithm to score game of HORSE in basketball given text string

n = 20
test1 = 'miss miss hit miss hit miss hit miss miss hit miss miss miss miss hit hit hit miss hit miss'

shots = test1.split(" ");

horse = "HORSE";

counter = 0;
p1_misses = 0;
p2_misses = 0;

while (counter < shots.length) {
    if (shots[counter] === "hit") {
        if(shots[counter+1] === "miss") {
            if((counter+1) % 2 === 0) {
                p1_misses +=1;
            } else {
                p2_misses += 1;
            }
        }
        counter += 2; 
    } else {
        counter += 1;
    }
    
}

console.log("Player 1: " + horse.slice(0, p1_misses));
console.log("Player 2: " + horse.slice(0, p2_misses));