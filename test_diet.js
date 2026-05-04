const dietPlans = [];
for(let i=0; i<15; i++) {
    let isRest = (i+1) % 7 === 0;
    let cals = isRest ? 2000 : 2200;
    let carbs = isRest ? 180 : 220;
    let type = isRest ? 'Rest Day' : 'Training Day';
    let macros = { cals: cals, prot: '180g', carb: carbs+'g', fat: '60g' };
    let micros = { iron: '15mg', calcium: '1000mg', vitD: '600 IU', zinc: '11mg' };
    
    let meals = [];
    if (!isRest) {
        meals = [
            { time: 'Breakfast', name: '5 whole eggs + 2 multigrain rotis + 1 cup milk', note: 'High protein morning anchor.', prot: '40g', color: 'var(--acc2)' },
            { time: 'Pre-workout', name: '1 banana + 30g oats + 1 scoop whey', note: 'Fast carbs + protein.', prot: '28g', color: 'var(--sky)' },
            { time: 'Post-workout', name: '1 scoop whey + 1 apple', note: 'Fast absorption.', prot: '25g', color: 'var(--grn)' },
            { time: 'Lunch', name: '200g paneer + 2 rotis + rajma + salad', note: 'Biggest meal. Max protein + fiber.', prot: '55g', color: 'var(--amb)' },
            { time: 'Dinner', name: '4 egg-whites + dal + 1 roti + sabzi', note: 'Low carb end of day.', prot: '35g', color: 'var(--acc)' }
        ];
    } else {
        meals = [
            { time: 'Breakfast', name: '4 whole eggs + 1 roti + milk', note: 'Slightly lower carbs.', prot: '35g', color: 'var(--acc2)' },
            { time: 'Lunch', name: '150g paneer + 2 rotis + salad', note: 'Moderate protein & fat.', prot: '40g', color: 'var(--amb)' },
            { time: 'Snack', name: 'Greek yogurt + almonds', note: 'Healthy fats & probiotics.', prot: '15g', color: 'var(--ora)' },
            { time: 'Dinner', name: 'Soya chunks sabzi + dal + 1 roti', note: 'High fiber, medium protein.', prot: '30g', color: 'var(--acc)' }
        ];
    }
    
    if (i%3===0) {
        meals[0].name = 'Oats porridge with whey + 3 boiled eggs';
        macros.cals += 50;
    } else if (i%4===0) {
        meals[meals.length-1].name = 'Chicken breast (150g) + veggies + 1 roti';
        macros.prot = '190g';
        micros.iron = '18mg';
    }
    
    dietPlans.push({ day: i+1, type: type, macros: macros, micros: micros, meals: meals });
}
console.log("No error!");
