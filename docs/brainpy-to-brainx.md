# BrainPy to BrainX

BrainPy was the early stage foundation of the **BrainX ecosystem**. It was
originally designed as a standalone package, before the other BrainX packages
existed. Today, BrainPy should be considered **a legacy package**: it remains
usable, but new projects should generally start with the corresponding BrainX
packages.

BrainX is the more complete modeling ecosystem with more variety of features
and better performance. Together, BrainX packages cover BrainPy's modeling and
simulation capabilities while providing a more complete foundation for modern
development.

## Where BrainPy fits

BrainPy is primarily a framework for **point-neuron network modeling,
simulation, and analysis**. In today's BrainX ecosystem, point-neuron modeling
is provided by **BrainPy-State**.

BrainPy is compatible with **BrainState**, **BrainCell**, **BrainMass**,
**BrainEvent**, and **BrainTools**. However, it is not compatible with
**BrainUnit** or **BrainTrace**. These two exceptions limit how fully a
BrainPy-based project can participate in the current ecosystem.

## Recommendation for point-neuron models

For new point-neuron models, use **BrainPy-State**. It provides the relevant
modeling capabilities in a form designed to work with the broader BrainX
ecosystem and its state, unit, event, and tracing infrastructure.

Existing BrainPy point-neuron projects do not need to be rewritten immediately.
If BrainPy already meets your needs, continuing to use it is reasonable.
Migration becomes more valuable when you need deeper integration with other
BrainX packages, stronger unit handling, newer infrastructure, or long-term
ecosystem support.

## Do not use BrainPy for cellular modeling

For biophysical neuron models involving **ions, ion channels, or neuronal
morphology**, migrate completely to **BrainPy-State + BrainCell**.

BrainPy's older ion and channel APIs have known design limitations, and its
compartmental modeling support is restricted to single-compartment models.
BrainCell is the BrainX package designed for conductance-based, ion-channel, and
morphologically structured cell models. Mixing the legacy BrainPy cell APIs
into new BrainCell-based work is therefore not recommended.

## The remaining BrainPy exception: analysis

BrainPy's **analysis module** is the main capability that does not yet have a
direct replacement elsewhere in the BrainX ecosystem. If your workflow depends
on this module, BrainPy may still be the appropriate tool for that part of the
project.

This is the important exception to the general migration guidance: BrainX
covers BrainPy's modeling and simulation roles, but BrainPy's dedicated
analysis functionality remains unique for now.

## Quick decision guide

| Your use case | Recommended choice |
| --- | --- |
| Starting a new point-neuron project | BrainPy-State |
| Maintaining an existing BrainPy project | Continue with BrainPy; migrate for integration |
| Modeling ions, ion channels, or morphology | BrainPy-State + BrainCell |
| Using BrainUnit or BrainTrace | Migrate away from BrainPy |
| Relying on BrainPy's analysis module | Continue using BrainPy for the analysis workflow |

## In short

Treat BrainPy as the legacy, early-stage form of the BrainX ecosystem. It is
still usable, especially for established point-neuron projects and its unique
analysis tools, but it is no longer the preferred starting point. Use
BrainPy-State for new point-neuron modeling, and use BrainPy-State together with
BrainCell for any work involving ions, channels, compartments, or morphology.
