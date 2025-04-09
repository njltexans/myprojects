document.getElementById("spin-button").addEventListener("click", function() {
    console.log("Spin button clicked!"); // Debugging log

    // Get bet amount from input
    const bet = parseInt(document.getElementById("bet").value);
    console.log("Bet amount:", bet); // Debugging log

    // Retrieve balance from local storage (default to 100 if not set)
    const balance = localStorage.getItem("balance") ? parseInt(localStorage.getItem("balance")) : 100;
    console.log("Current balance:", balance); // Debugging log

    const lines = 3; // Default to 3 lines

    // Fetch request to backend API
    fetch("https://myprojects-5ry5.onrender.com/spin", {  //Render URL
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ balance: balance, lines: lines, bet: bet })
    })
    .then(response => {
        console.log("Fetch Response Status:", response.status); // Debugging log

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        return response.json();
    })
    .then(data => {
        console.log("Fetch Response Data:", data); // Debugging log

        if (data.error) {
            document.getElementById("result").innerText = data.error;
            return;
        }

        // Update reels display
        document.getElementById("reel1").innerText = data.reels[0][0];
        document.getElementById("reel2").innerText = data.reels[1][0];
        document.getElementById("reel3").innerText = data.reels[2][0];

        // Display winnings and update balance
        document.getElementById("result").innerText = `You won $${data.winnings}`;
        localStorage.setItem("balance", data.new_balance);
    })
    .catch(error => {
        console.error("Fetch error:", error);
        document.getElementById("result").innerText = "Error connecting to server.";
    });
});


