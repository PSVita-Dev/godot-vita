
import os
import sys
import platform
#Some stuff taken from godot-switch by fhidalgosola

def is_active():
	return True

def get_name():
        return "psvita"


def can_build():

	if ("VITASDK" not in os.environ):
		return False
	if (os.name=="nt"):
		return False
	
	return True

def get_opts():

	return [
	('debug_release', 'Add debug symbols to release version','no'),
	]

def get_flags():

    return [
        ('builtin_squish', 'no'),
        ('tools', 'no'),
    ]

def configure(env):
    
    vitasdk_path = os.environ.get("VITASDK")
    compiler_tools_path = vitasdk_path + "/arm-vita-eabi/bin"
    compiler_path = vitasdk_path + "/bin/"
    pkg_config_path = vitasdk_path + "/arm-vita-eabi/lib/pkgconfig/pkgconfig"

    env['ENV']['VITASDK'] = vitasdk_path  # used in linking stage
    os.environ["PKG_CONFIG_PATH"] = pkg_config_path
    env['ENV']['PKG_CONFIG_PATH'] = pkg_config_path

    env["RANLIB"] = compiler_path + "arm-vita-eabi-ranlib"
    env["AR"] = compiler_path + "arm-vita-eabi-ar"
    env["LD"] = compiler_path + "arm-vita-eabi-g++"
    env['CC'] = compiler_path + "arm-vita-eabi-gcc"
    env['CXX'] = compiler_path + "arm-vita-eabi-g++"
	

    ## Build type
    if (env["target"] == "release"):
        if (env["optimize"] == "speed"): #optimize for speed (default)
            env.Prepend(CCFLAGS=['-O3'])
        else: #optimize for size
            env.Prepend(CCFLAGS=['-Os'])

        if (env["debug_symbols"] == "yes"):
            env.Prepend(CCFLAGS=['-g1'])
        if (env["debug_symbols"] == "full"):
            env.Prepend(CCFLAGS=['-g2'])
    elif (env["target"] == "release_debug"):
        if (env["optimize"] == "speed"): #optimize for speed (default)
            env.Prepend(CCFLAGS=['-O2', '-DDEBUG_ENABLED'])
        else: #optimize for size
            env.Prepend(CCFLAGS=['-Os', '-DDEBUG_ENABLED'])

        if (env["debug_symbols"] == "yes"):
            env.Prepend(CCFLAGS=['-g1'])
        if (env["debug_symbols"] == "full"):
            env.Prepend(CCFLAGS=['-g2'])
    elif (env["target"] == "debug"):
        env.Prepend(CCFLAGS=['-std=c++11','-g3','-unsafe', '-DDEBUG_ENABLED', '-DDEBUG_MEMORY_ENABLED'])
		#env.Prepend(CXXFLAGS=["-Wl,-q"])
    ## Architecture
    ARCH = ["-march=armv9-a", "-mtune=cortex-a9", "-mtp=soft"]
    env["bits"] = "32"
    env["arch"] = "arm"
    env.Append(CPPPATH=["#platform/vita"])
    env.Append(
        CPPFLAGS=[
           # "-DOPENGL_ENABLED",
            "-DGLES2_ENABLED",
            #"-DPTHREAD_ENABLED",
           # "-DUNIX_ENABLED",
            "-DLIBC_FILEIO_ENABLED",
            
        ]
		)
	#
	
    ## Compiler configuration
	#env.Append(CFLAGS=['-Wl','-q'])
	#env.Append(CFLAGS=[-Wl -q])
    env.Append(CCFLAGS=["-Wl,-q",'-unsafe'])
    env.Append(LINKFLAGS=['-lpib',"-Wl,-q",'-unsafe','-lSceLibKernel_stub'
  #,'-lSceThreadmgr_stub'
  #,'-lSceModulemgr_stub'
  ,'-lSceSysmodule_stub'
  ,'-lSceIofilemgr_stub'
  ,'-lSceGxm_stub'
  ,'-lSceDisplay_stub'
  ,'-lSceLibc_stub'])
  #,'-lSceLibm_stub'])
   # env.Append(CXXFLAGS=['-Wl' ,'-q'])
	#'-Wl','-q',
#"-DVITA_ENABLED",
#,' -lSceShaccCg_stub'
