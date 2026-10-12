#pragma once

#include <string>

class Notification {
public:
    /*
     * virtual lets C++ choose a function based on the actual object’s type, 
     * even when you access it through a base-class pointer.
     * For example, a Notification* can point to an EmailNotification.
     * If send() is virtual, calling it through that pointer runs EmailNotification::send().
     * If you delete derived objects through a base-class pointer,
     * the base class must have a virtual destructor.
     */
    virtual ~Notification() = default;
    
    /*
     * The "= 0" marks the function as pure virtual, which makes this class abstract.
     * 
     * A pure virtual function declares a function that inherited classes must implement
     * to become concrete classes. Here, every class that inherits Notification should
     * implement send(), though Notification itself does not provide a concrete implementation.
     * 
     * A class that contains at least one pure virtual function is considered abstract,
     * and we cannot instantiate an abstract class directly.
     
     * Here, we cannot instantiate Notification directly.
     * But it is still possible to use Notification* pointer for
     * inherited classes like EmailNotification.
     */
    virtual void send(std::string message) = 0;
};