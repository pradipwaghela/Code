#include <gtk/gtk.h>
int main(int argc, char *argv[]) {
    GtkWidget *windows;
 gtk_init(&argc, &argv);
 windows = gtk_window_new(GTK_WINDOW_TOPLEVEL);
gtk_container_set_border_width(GTK_CONTAINER(windows), 20);
gtk_widget_show_all(windows);
gtk_main();

        
    return 0;
}