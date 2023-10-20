CXXFLAGS = -Wall -Wextra -O3 --std=c++23

main: main.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

