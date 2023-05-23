app.on('ready', () => {
    const mainWindow = new BrowserWindow({
      // Window options
      width: 800,
      height: 600,
      webPreferences: {
        nodeIntegration: true
      }
    });
  
    mainWindow.loadFile('index.html');
  });

  
  ipcMain.on('formSubmission', (event, formData) => {
    // Process the form data and create the JSON object
    const jsonObject = {
      // Assign values from formData to respective JSON properties
    };
  
    // Write the JSON object to a file or perform further actions
    // based on your requirements
  });

  
  // In the renderer process (index.html)
const { ipcRenderer } = require('electron');

// Triggered when the form is submitted
function submitForm() {
  // Collect the form data

  // Send the form data to the main process
  ipcRenderer.send('formSubmission', formData);
}
