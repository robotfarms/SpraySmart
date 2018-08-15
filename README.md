## WeedSmart
A weed detection and spraying system using the OpenMV camera and machine vision

**Background (can skip)**
So I'm a farmer over here in Australia and we grow a heap of crops. We grow them through the winter, then through the summer, we have fallow (bare) paddocks with only left over wheat or canola stubble in them. We spray these paddocks for weeds in an effort to conserve moisture for the following crops as we are in a low rainfall area, and every little bit of moisture helps. Currently we blanket spray with herbicides, spraying every inch of the paddock trying to kill the growing weeds that suck moisture and nutrients from the soil. But there is a better way.

**On to the proposed project**
What I want to do it find the green weeds in a paddock, and spray them individually using an OpenMV camera, coupled with an optocoupler mosfet or relay and a pressurised solenoid with spray nozzle.

**Here are some details of a few things:**
* Monitor about a 1m wide patch of ground
* Have that 1m patch split into 2 sectors (left and right) that then triggers a left or right sprayer
* Detect green or greenish weeds on a fairly uniform straw or dirt background
  * The weeds don't need to be tracked, but I think just detecting of green is present in the frame (and sector) will be enough
  * There may be a few ranges, or broad range of greens to find
* Trigger the 12v solenoid via a relay (PWM, MOSFET or regular 3.3 triggered)
* Chemical then flows through the solenoid, and spray nozzle, spraying the weed
* The plan is to have one every meter over a 36 meter boom so 36 camera and solenoid modules
* Each module will have its own enclosure
* Ultimately (if possible) I would like to also have each one linked somehow to a monitor in the cab of the tractor/sprayer displaying the status of each one
* Everything will be open source, including plans for a modular spray trailer, wiring and fluid diagrams and anything else I come across
* Ultimately the ultimate will be to have this system on a fully autonomous vehicle using a Pixhawk autopilot and ROS operating system

There are other similar commercial systems out there, such as the [WeediT](www.weedit.com) system which I believe used a chlorophyll sensor and works quite well. For a 36m wide system we are looking at around $360,000(AUD), so they are a bit cost prohibitive for your average farmer. They do however claim to use only 10% of the chemical that you would otherwise use if you blanket spray an area. When we spend well over $100,000 on herbicides each year, the savings can be significant.

I plan on making everything open source, and freely available. I believe this would benefit many farmers and the environment, saving thousands of litres of chemical and therefore dollars. Where there is a risk of chemical run off, it would reduce the chemical in the system too as well as spray drift.

If you made it through all that I hope it makes sense, if anyone has any questions or needs me to clarify things, shoot away.
