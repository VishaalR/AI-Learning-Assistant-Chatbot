async function sendMessage() {

    const inputField =
        document.getElementById("user-input");

    const chatBox =
        document.getElementById("chat-box");

    const typing =
        document.getElementById("typing");

    const userMessage =
        inputField.value.trim();

    if (userMessage === "") return;

    // User Message
    addMessage(userMessage, "user");

    inputField.value = "";

    typing.style.display = "block";

    // Fetch Response
    const response = await fetch("/get_response", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: userMessage
        })
    });

    const data = await response.json();

    setTimeout(() => {

        typing.style.display = "none";

        addMessage(data.response, "bot");

    }, 700);
}

function addMessage(message, sender) {

    const chatBox =
        document.getElementById("chat-box");

    const messageDiv =
        document.createElement("div");

    messageDiv.classList.add(
        "message",
        `${sender}-message`
    );

    const avatar =
        sender === "bot" ? "🤖" : "🧑";

    messageDiv.innerHTML = `

        <div class="avatar">
            ${avatar}
        </div>

        <div class="message-content">
            ${message}
        </div>
    `;

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop =
        chatBox.scrollHeight;
}

document
.getElementById("user-input")
.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {

        sendMessage();
    }
});