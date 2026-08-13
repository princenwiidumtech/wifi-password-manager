from wifi_manager import save_wifi, view_wifi

print("Saving Wi-Fi...")
save_wifi("Home WiFi", "MyPassword123")

print("\nSaved Wi-Fi networks:")
view_wifi()