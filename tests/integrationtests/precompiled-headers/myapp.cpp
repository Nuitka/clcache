// MYAPP.CPP : Sample application
//             All precompiled code other than the file listed
//             in the makefile's BOUNDARY macro (stable.h in
//             this example) must be included before the file
//             listed in the BOUNDARY macro. Unstable code must
//             be included after the precompiled code.
//
#include "another.h"
#include "stable.h"
#include "unstable.h"

int main()
{
    savetime();
    savemoretime();
    notstable();
    return 0;
}
