#include <limits.h>
#include <stdlib.h>
#include <unistd.h>

#include "main/main.h"
#include "os_vita.h"

int main(int argc, char *argv[]) {

	OS_VITA OS;
	char* args[] = {"-path", "ux0:/data/godot"};

	Error err = Main::setup(argv[0], argc - 1, &argv[1]);
	if (err != OK) {
//		free(cwd);
		return 255;
	}

	if (Main::start())
		OS.run(); // it is actually the OS that decides how to run
	Main::cleanup();

//	chdir(cwd);
//	free(cwd);

	return 0;
}
