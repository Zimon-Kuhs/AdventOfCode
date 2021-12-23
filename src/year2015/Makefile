APP             =  adventOfCode
BASE_DIR        =  $(shell pwd)
INCLUDES        =  $(shell find $(SRC_DIR) -type d)
OBJS            =  $(shell find $(SRC_DIR) -name "*.c")
SRC_DIR         =  . ../../test

####    Build library flags.    ####

PKGS = check
CFLAGS  += $(shell PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) pkg-config --cflags $(PKGS))
LDLIBS  += $(shell PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) pkg-config --libs $(PKGS))
CFLAGS  += $(addprefix -I,$(INCLUDES))

INCLUDE_FILES = $(addprefix -I, $(INCLUDES))

####   Compiler flags.   ####

CFLAGS  += -pedantic \
            -O2 \
            -W \
            -Wall \
            -Wdisabled-optimization \
            -Werror \
            -Wfloat-equal \
            -Wformat=2 \
            -Winline \
            -Wpedantic \
            -Wpointer-arith

all: $(APP)

$(APP): $(OBJS)
	$(CXX) $(CFLAGS) $(CPPFLAGS) $^ $(INCLUDE_FILES) $(LIBS) $(LDLIBS) $(SHARED_LIBS) $(CONSTANTS) -o $@

clean:
	rm -f $(APP) *.o core *.eap*
	rm -rf build
