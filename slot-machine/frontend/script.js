document.getElementById("spin-button").addEventListener("click", function() {
    const bet = parseInt(document.getElementById("bet").value);
    const balance = localStorage.getItem("balance") ? parseInt(localStorage.getItem("balance")) : 100;
    const lines = 3; // Default to 3 lines

    fetch("https://myprojects-5ry5.onrender.com/spin", {  // <-- Replace with your Render backend URL
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            balance: balance,
            lines: lines,
            bet: bet
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = data.error;
            return;
        }

        document.getElementById("reel1").innerText = data.reels[0][0];
        document.getElementById("reel2").innerText = data.reels[1][0];
        document.getElementById("reel3").innerText = data.reels[2][0];

        document.getElementById("result").innerText = `You won $${data.winnings}`;
        localStorage.setItem("balance", data.new_balance);
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error connecting to server.";
    });
});

