RM = @del /q

OBJS = myapp.obj applib.obj
APP = myapp.exe

# List all stable header files in the STABLEHDRS macro.
STABLEHDRS = stable.h another.h

# List the final header file to be precompiled here:
BOUNDARY = stable.h

# List header files under development here:
UNSTABLEHDRS = unstable.h

CPPFLAGS  = /nologo /EHsc /c /W3 /Gs /MT
LINKFLAGS =
LIBS      =

$(APP): $(OBJS)
    link $(LINKFLAGS) /OUT:$(APP) $(OBJS) $(LIBS)

# Compile myapp
myapp.obj  : myapp.cpp $(UNSTABLEHDRS)  stable.pch
    $(CPP) $(CPPFLAGS) /Yu$(BOUNDARY) myapp.cpp

# Compile applib
#the_applib.obj : applib.cpp $(UNSTABLEHDRS) stable.pch
#    $(CPP) $(CPPFLAGS) /Yu$(BOUNDARY) /Fothe_applib.obj applib.cpp

# Compile headers
stable.pch : $(STABLEHDRS)
    $(CPP) $(CPPFLAGS) /Yc$(BOUNDARY) applib.cpp

.PHONY: clean

clean:
    $(RM) $(OBJS) $(APP) stable.pch
