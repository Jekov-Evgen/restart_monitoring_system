#include "pch.h"
#include "memory.h"
#include "Windows.h"

extern "C" __declspec(dllexport) float GetMemory()
{
	MEMORYSTATUSEX dataComputer;
	dataComputer.dwLength = sizeof(MEMORYSTATUSEX);

	if (GlobalMemoryStatusEx(&dataComputer)) {
		return static_cast<float>(dataComputer.dwMemoryLoad);
	}
	else {
		return -1.0f;
	}
}