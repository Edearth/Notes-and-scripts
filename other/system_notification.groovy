import java.awt.*
import java.awt.event.*
import java.awt.SystemTray.*

public class Notification {
  static Image image = Toolkit.getDefaultToolkit().getImage("C:\\Users\\test\\Pictures\\icon.png");

  static TrayIcon trayIcon = new TrayIcon(image, "Tester2");

  public static void displayMessage(String title, String message) throws Exception {
    new Thread(new Runnable()
    {
    	 @Override
      public void run() {
        if (SystemTray.isSupported()) {
          SystemTray tray = SystemTray.getSystemTray()
          trayIcon.setImageAutoSize(true)

          try {
            tray.add(trayIcon)
          } catch (AWTException e) {
            System.err.println("TrayIcon could not be added.")
          }

          trayIcon.displayMessage(title, message, TrayIcon.MessageType.INFO)
          sleep(30000)
          tray.remove(trayIcon)
        }
      }
    }).start()
  }
}


context.setProperty("notification", new Notification())