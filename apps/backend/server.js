const PORT = process.env.PORT || 4000;

function startServer() {
  console.log(`Backend server scaffold ready on port ${PORT}`);
}

if (require.main === module) {
  startServer();
}

module.exports = { startServer };
